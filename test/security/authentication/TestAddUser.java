package security.authentication;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertNotNull;
import static org.junit.Assert.assertTrue;
import static org.junit.Assert.assertFalse;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.security.NoSuchAlgorithmException;
import java.text.ParseException;
import java.util.Base64;
import java.util.List;

import org.junit.Before;
import org.junit.After;
import org.junit.Test;

import security.authentication.AddUser;
import security.cryptography.PasswordChecker;
import utils.CSVReader;

/**
 * Test cryptographic functions with a testing database
 */
public class TestAddUser {
    private String testCSV = "test/testHashedLogins.csv";

    @Before
    public void setup() throws IOException{
        File testFile = new File(testCSV);
        testFile.delete();
        FileWriter testWriter = new FileWriter(testFile);
        testWriter.write("username,sid,salt,passwordhash\n");
        testWriter.close();
    }

    @After
    public void cleanup() throws IOException{
        File testFile = new File(testCSV);
        testFile.delete();
    }

    /**
     * Try adding users and verifying they are correctly added to the database
     * @throws FileNotFoundException Sample logins are not provided
     * @throws IOException CSV file not opened correctly
     * @throws NoSuchAlgorithmException Problem with generating salts
     */
    @Test
    public void testAddUser() throws FileNotFoundException, IOException, NoSuchAlgorithmException {
        List<List<String>> logins = CSVReader.readCSV("data/logins.csv");
        for (int i = 1; i < logins.size(); i++) {
            List<String> login = logins.get(i);
            AddUser newUser = new AddUser(login.get(0), login.get(2), login.get(1), testCSV);
            assertTrue(newUser.addUser());
            List<String> newLogin = CSVReader.readCSV(testCSV).getLast();
            byte[] salt = Base64.getDecoder().decode(newLogin.get(2));
            assertTrue(PasswordChecker.verifyPassword(login.get(1), salt, newLogin.get(3)));
            assertEquals(newLogin.get(0), login.get(0));
            assertEquals(newLogin.get(1), login.get(2));
        }
    }

    /**
     * Try creating users with strange passwords (weird characters)
     * @throws FileNotFoundException Sample logins are not provided
     * @throws IOException CSV file not opened correctly
     * @throws NoSuchAlgorithmException Problem with generating salts
     */
    @Test
    public void testStrangeCharacters() throws FileNotFoundException, IOException, NoSuchAlgorithmException {
        String[] weirdCharacters = new String[]{"\'", "\\", ";", "@", "[]", "\"", ",", "."};
        for (int i = 0; i < weirdCharacters.length; i++) {
            AddUser newUser = new AddUser(String.valueOf(i), String.valueOf(i), weirdCharacters[i], testCSV);
            assertTrue(newUser.addUser());
            List<String> newLogin = CSVReader.readCSV(testCSV).getLast();
            byte[] salt = Base64.getDecoder().decode(newLogin.get(2));
            assertTrue(PasswordChecker.verifyPassword(weirdCharacters[i], salt, newLogin.get(3)));
            assertEquals(newLogin.get(0), String.valueOf(i));
            assertEquals(newLogin.get(1), String.valueOf(i));
        }
    }

    /**
     * Try adding duplicate users and it should not be accepted
     * @throws FileNotFoundException Sample logins are not provided
     * @throws IOException CSV file not opened correctly
     * @throws NoSuchAlgorithmException Problem with generating salts
     */
    @Test
    public void testDuplicateUsers() throws FileNotFoundException, IOException, NoSuchAlgorithmException {
        String user = "user";
        String user2 = "user2";
        String sid = "1000";
        String sid2 = "2000";
        String password = "password";
        
        AddUser firstUser = new AddUser(user, sid, password, testCSV);
        assertTrue(firstUser.addUser());

        AddUser dupSid = new AddUser(user2, sid, password, testCSV);
        assertFalse(dupSid.addUser());

        AddUser dupName = new AddUser(user, sid2, password, testCSV);
        assertFalse(dupName.addUser());

        AddUser dupeBoth = new AddUser(user, sid, password, testCSV);
        assertFalse(dupeBoth.addUser());
    }
}
