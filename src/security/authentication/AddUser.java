package security.authentication;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.PrintWriter;
import java.security.NoSuchAlgorithmException;
import java.util.Base64;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.Stream;

import security.cryptography.PasswordChecker;
import utils.CSVReader;

/**
 * Add a new user to the login database using this class.
 * First create an instance of the class, then call addUser().
 */
public class AddUser {
    private String CSV_FILE_NAME = "resources/hashedLogins.csv";
    private String username;
    private String password;
    private String sid;

    /**
     * Creates a new user to be added
     * @param username The username to be added
     * @param sid The student ID for the new user
     * @param password The password (plaintext) for the user to be added
     */
    public AddUser(String username, String sid, String password) {
        this.username = username;
        this.password = password;
        this.sid = sid;
    }

    /**
     * Creates a new user to add to csvpath.
     * @param username The username to be added
     * @param sid The student ID for the new user
     * @param password The password (plaintext) for the user to be added
     * @param csvpath Column order should be username, sid, salt, passwordhash
     */
    public AddUser(String username, String sid, String password, String csvpath) {
        this.username = username;
        this.password = password;
        this.sid = sid;
        this.CSV_FILE_NAME = csvpath;
    }

    /**
     * Adds this user to the login database
     * @return true if the user is correctly added, false if the username/SID is already in the system
     * @throws IOException The csv file was not correctly opened
     * @throws NoSuchAlgorithmException The salt for the hash was not correctly generated
     */
    public boolean addUser() throws IOException, NoSuchAlgorithmException {
        String[] newUser = new String[4];
        newUser[0] = username;
        newUser[1] = sid;
        if (!verifyUniqueUser()) {
            return false;
        }
        byte[] salt;
        salt = PasswordChecker.generateSalt(); 
        newUser[2] = Base64.getEncoder().encodeToString(salt);
        newUser[3] = PasswordChecker.hashPassword(password, salt);
        appendCSV(newUser);
        return true;
    }

    /**
     * We validate the user details are not overlapping with an existing username/sid
     * @return true if the username/sid are unique, false otherwise
     * @throws FileNotFoundException The CSV file could not be opened.
     */
    private boolean verifyUniqueUser() throws FileNotFoundException {
        List<List<String>> existing = CSVReader.readCSV(CSV_FILE_NAME);
        for (int i = 1; i < existing.size(); i++) {
            if (existing.get(i).get(0).equals(username) || existing.get(i).get(1).equals(sid)) {
                return false;
            }
        }
        return true;
    }

    /**
     * Convert string array to csv format
     * Created using tutorial: https://www.baeldung.com/java-csv
     * @param data String array to be converted to line for csv file
     * @return String as comma concatenated version of data with special characters escaped
     */
    private String convertToCSV(String[] data) {
        return Stream.of(data)
        .map(this::escapeSpecialCharacters)
        .collect(Collectors.joining(","));
    }

    /**
     * Add line to CSV
     * Created using tutorial: https://www.baeldung.com/java-csv
     * @param data String array to be converted to line for csv file
     * @return String as comma concatenated version of data with special characters escaped
     */
    private void appendCSV(String[] data) throws IOException {
        File csvOutputFile = new File(CSV_FILE_NAME);
        try (PrintWriter pw = new PrintWriter(new FileOutputStream(csvOutputFile, true))) {
            String newLine = convertToCSV(data);
            pw.println(newLine);
        }
    }

    /**
     * Remove special characters from string by ecsaping them
     * Created using tutorial: https://www.baeldung.com/java-csv
     * @param data String to be formatted
     * @return Formatted version of string
     */
    private String escapeSpecialCharacters(String data) {
        if (data == null) {
            throw new IllegalArgumentException("Input data cannot be null");
        }
        String escapedData = data.replaceAll("\\R", " ");
        if (data.contains(",") || data.contains("\"") || data.contains("'")) {
            data = data.replace("\"", "\"\"");
            escapedData = "\"" + data + "\"";
        }
        return escapedData;
    }
}
