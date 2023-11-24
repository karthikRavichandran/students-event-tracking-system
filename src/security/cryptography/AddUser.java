package security.cryptography;

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

import utils.CSVReader;

public class AddUser {
    private String CSV_FILE_NAME = "resources/hashedLogins.csv";
    private String username;
    private String password;
    private String sid;

    public AddUser(String username, String sid, String password) {
        this.username = username;
        this.password = password;
        this.sid = sid;
    }

    public AddUser(String username, String sid, String password, String csvpath) {
        this.username = username;
        this.password = password;
        this.sid = sid;
        this.CSV_FILE_NAME = csvpath;
    }

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

    private boolean verifyUniqueUser() throws FileNotFoundException {
        List<List<String>> existing = CSVReader.readCSV(CSV_FILE_NAME);
        for (int i = 1; i < existing.size(); i++) {
            if (existing.get(i).get(0).equals(username) || existing.get(i).get(1).equals(sid)) {
                return false;
            }
        }
        return true;
    }

    private String convertToCSV(String[] data) {
        return Stream.of(data)
        .map(this::escapeSpecialCharacters)
        .collect(Collectors.joining(","));
    }

    private void appendCSV(String[] data) throws IOException {
        File csvOutputFile = new File(CSV_FILE_NAME);
        try (PrintWriter pw = new PrintWriter(new FileOutputStream(csvOutputFile, true))) {
            String newLine = convertToCSV(data);
            pw.println(newLine);
        }
    }

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
