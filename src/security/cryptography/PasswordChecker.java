package security.cryptography;

import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.security.SecureRandom;
import java.util.Base64;

public class PasswordChecker {

    /**
     * Hash a given password using SHA-256 and the provided salt.
     * @param password The plaintext password to be hashed
     * @param salt The salt to combine with the hash function
     * @return Returns the hashed version of the password
     */
    protected static String hashPassword(String password, byte[] salt) {
        String generatedPassword = null;
        try {
            MessageDigest md = MessageDigest.getInstance("SHA-256");
            md.update(salt);
            byte[] bytes = md.digest(password.getBytes());
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < bytes.length; i++) {
                sb.append(Integer.toString((bytes[i] & 0xff) + 0x100, 16).substring(1));
            }
            generatedPassword = sb.toString();
        } catch (NoSuchAlgorithmException e) {
            e.printStackTrace();
        }
        return generatedPassword;
    }

    /**
     * Generates a random byte array for salting hash functions
     * @return Hash function to salt
     * @throws NoSuchAlgorithmException There was a problem with generating a random array
     */
    public static byte[] generateSalt() throws NoSuchAlgorithmException {
        SecureRandom random = new SecureRandom();
        byte[] salt = new byte[16];
        random.nextBytes(salt);
        return salt;
    }

    /**
     * Validate a password/salt combo with a hashed password
     * @param password Password to validate
     * @param salt Salt to combo with the password
     * @param hashedPassword Intended matching hashed password
     * @return true if the password/salt matches hashed password
     */
    public static boolean verifyPassword(String password, byte[] salt, String hashedPassword) {
        return hashedPassword.equals(hashPassword(password, salt));
    }
    /**
     * Validate a password/salt combo with a hashed password
     * @param password Password to validate
     * @param salt Salt to combo with the password
     * @param hashedPassword Intended matching hashed password
     * @return true if the password/salt matches hashed password
     */
    public static boolean verifyPassword(String password, String salt, String hashedPassword) {
        return hashedPassword.equals(hashPassword(password, Base64.getDecoder().decode(salt)));
    }
    

}
