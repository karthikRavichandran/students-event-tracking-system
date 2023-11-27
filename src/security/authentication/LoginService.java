package security.authentication;
import java.io.IOException;
import java.security.NoSuchAlgorithmException;

import javax.security.auth.Subject;
import javax.security.auth.login.LoginContext;
import javax.security.auth.login.LoginException;
import javax.security.auth.callback.CallbackHandler;

import security.authentication.ConsoleCallbackHandler;

/**
 * Based on tutorial: https://www.baeldung.com/java-authentication-authorization-service
 * Actual service object, create and call login to log in a user. To add a user, call addNewUser
 */
public class LoginService {

    /**
     * Uses default handler (console) for logins
     * @return Subject which has logged in succesfully
     * @throws LoginException When login has failed (wrong username/password combo)
     */
    public Subject login() throws LoginException {
        LoginContext loginContext = new LoginContext("jaasApplication", new ConsoleCallbackHandler());
        loginContext.login();
        return loginContext.getSubject();
    }

    /**
     * Uses specified handler (console) for logins
     * @param handler CallbackHandler to use for password/username
     * @return Subject which has logged in succesfully
     * @throws LoginException When login has failed (wrong username/password combo)
     */
    public Subject login(CallbackHandler handler) throws LoginException {
        LoginContext loginContext = new LoginContext("jaasApplication", handler);
        loginContext.login();
        return loginContext.getSubject();
    }

    /**
     * Add a new user to our system, with given user, password, student id.
     * @param username Username for the new user
     * @param password Password (plaintext) for the new user
     * @param sid Student ID for new user
     * @return true if the creation is successful, false otherwise (e.g. duplicated users)
     * @throws IOException CSV file is not found
     * @throws NoSuchAlgorithmException Salt generation failure
     */
    public boolean addNewUser(String username, String password, String sid) throws IOException, NoSuchAlgorithmException {
        AddUser newUser = new AddUser(username, sid, password);
        return newUser.addUser();
    }
}