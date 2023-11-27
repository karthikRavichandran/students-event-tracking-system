package security.authentication;
import com.sun.security.auth.UserPrincipal;

import security.cryptography.PasswordChecker;
import utils.CSVReader;

import javax.security.auth.Subject;
import javax.security.auth.callback.*;
import javax.security.auth.login.LoginException;
import javax.security.auth.spi.LoginModule;

import java.io.FileNotFoundException;
import java.io.IOException;
import java.security.Principal;
import java.util.List;
import java.util.Map;

/**
 * Based on tutorial: https://www.baeldung.com/java-authentication-authorization-service
 * Class that tries to log in a user based on the stored login database
 */
public class Login implements LoginModule {

    private Subject subject;
    private CallbackHandler callbackHandler;

    private String username;
    private boolean loginSucceeded = false;
    private Principal userPrincipal;

    private String CSV_FILE_NAME = "resources/hashedLogins.csv";

    /**
     * Reads the login database and gets corresponding username, sid, salt, password hash as String
     * @param username username of user to read in
     * @return List of 4 {username, sid, salt, passwordhash}
     * @throws FileNotFoundException Unable to read hashed login database
     */
    private List<String> getDatabaseCred (String username) throws FileNotFoundException {
        List<List<String>> loginData = CSVReader.readCSV(CSV_FILE_NAME);
        for (int i = 1; i < loginData.size(); i++) {
            if (loginData.get(i).get(0).equals(username)) {
                return loginData.get(i);
            }
        }
        return null;
    }

    @Override
    public void initialize(Subject subject, CallbackHandler callbackHandler, Map<String, ?> sharedState,
                           Map<String, ?> options) {
        this.subject = subject;
        this.callbackHandler = callbackHandler;
    }

    @Override
    public boolean login() throws LoginException {
        NameCallback nameCallback = new NameCallback("username: ");
        PasswordCallback passwordCallback = new PasswordCallback("password: ", false);
        try {
            callbackHandler.handle(new Callback[]{nameCallback, passwordCallback});
            username = nameCallback.getName();
            String password = new String(passwordCallback.getPassword());
            
            List<String> hashedData = getDatabaseCred(username);
            if (hashedData == null) {
                loginSucceeded = false;
            } else if (PasswordChecker.verifyPassword(password, hashedData.get(2), hashedData.get(3))) {
                loginSucceeded = true;
            } else {
                loginSucceeded = false;
            }
        } catch (IOException | UnsupportedCallbackException e) {
            throw new LoginException("Can't login");
        }
        return loginSucceeded;
    }

    @Override
    public boolean commit() throws LoginException {
        if (!loginSucceeded) {
            return false;
        }
        userPrincipal = new UserPrincipal(username);
        subject.getPrincipals().add(userPrincipal);
        return true;
    }

    @Override
    public boolean abort() throws LoginException {
        logout();
        return true;
    }

    @Override
    public boolean logout() throws LoginException {
        subject.getPrincipals().remove(userPrincipal);
        return false;
    }
}