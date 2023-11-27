package security.cryptography;

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
 * Test cryptographic functions
 */
public class TestPassword {

    /**
     * Try valid password/salt combintations
     * @throws FileNotFoundException Sample logins are not provided
     * @throws IOException CSV file not opened correctly
     * @throws NoSuchAlgorithmException Problem with generating salts
     */
    @Test
    public void testValidPassword() throws FileNotFoundException, IOException, NoSuchAlgorithmException {
        byte[] salt = PasswordChecker.generateSalt();
        byte[] salt2 = PasswordChecker.generateSalt();
        String password = "password";
        String hash1 = PasswordChecker.hashPassword(password, salt);
        String hash2 = PasswordChecker.hashPassword(password, salt2);

        assertTrue(PasswordChecker.verifyPassword(password, salt, hash1));
        assertTrue(PasswordChecker.verifyPassword(password, salt, hash2));
    }

    /**
     * Try false password/salt combintations
     * @throws FileNotFoundException Sample logins are not provided
     * @throws IOException CSV file not opened correctly
     * @throws NoSuchAlgorithmException Problem with generating salts
     */
    @Test
    public void testInvalidPassword() throws FileNotFoundException, IOException, NoSuchAlgorithmException {
        byte[] salt = PasswordChecker.generateSalt();
        byte[] salt2 = PasswordChecker.generateSalt();
        String password = "password";
        String trueHash = PasswordChecker.hashPassword(password, salt);
        String falseHash = PasswordChecker.hashPassword(password, salt2);

        assertFalse(PasswordChecker.verifyPassword(password, salt2, trueHash));
        assertTrue(PasswordChecker.verifyPassword(password, salt, trueHash));
        assertFalse(PasswordChecker.verifyPassword("PASSWORD", salt, trueHash));
    }
}
