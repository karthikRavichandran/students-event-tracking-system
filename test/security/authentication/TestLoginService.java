package security.authentication;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertNotNull;
import static org.junit.Assert.assertTrue;
import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertThrows;

import java.io.ByteArrayInputStream;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStream;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.security.NoSuchAlgorithmException;
import java.text.ParseException;
import java.util.Base64;
import java.util.List;

import javax.security.auth.Subject;
import javax.security.auth.callback.Callback;
import javax.security.auth.callback.CallbackHandler;
import javax.security.auth.callback.NameCallback;
import javax.security.auth.callback.PasswordCallback;
import javax.security.auth.callback.UnsupportedCallbackException;
import javax.security.auth.login.LoginException;

import org.junit.Before;
import org.junit.After;
import org.junit.Test;

import security.authentication.LoginService;
import utils.CSVWriter;

/**
 * Integrated tests that use real username/password combos in our synthetic data
 */
public class TestLoginService {

    @Before
    public void setup() {
        System.setProperty("java.security.auth.login.config", "resources/jaas.login.config");
    }

    @Test
    public void testLoginSuccess() throws LoginException {
        LoginService loginService = new LoginService();
        TestHandler testHandler = new TestHandler();
        testHandler.setTestUsername("alice");
        testHandler.setTestPassword("alicepw");
        Subject subject = loginService.login(testHandler);
        assertNotNull(subject);
    }

    @Test
    public void testLoginFail() throws LoginException {
        LoginService loginService = new LoginService();
        TestHandler testHandler = new TestHandler();
        testHandler.setTestUsername("alice");
        testHandler.setTestPassword("wrong password");
        assertThrows(LoginException.class, () -> loginService.login(testHandler));
    }

    @Test
    public void createNewUserDuplicateFail() throws LoginException, IOException, NoSuchAlgorithmException {
        LoginService loginService = new LoginService();
        TestHandler testHandler = new TestHandler();
        assertFalse(loginService.addNewUser("alice", "alicepw", "5000"));
        assertFalse(loginService.addNewUser("alice", "other", "5000"));
        assertFalse(loginService.addNewUser("other", "other", "1001"));
    }

    @Test
    public void createNewUserSuccess() throws LoginException, IOException, NoSuchAlgorithmException {
        LoginService loginService = new LoginService();
        TestHandler testHandler = new TestHandler();
        testHandler.setTestUsername("test");
        testHandler.setTestPassword("testpw");
        assertTrue(loginService.addNewUser("test", "testpw", "testid"));
        assertNotNull(loginService.login(testHandler));
        CSVWriter.removeRow(-1, "resources/hashedLogins.csv");
        assertThrows(LoginException.class, () -> loginService.login(testHandler));
    }

    /**
     * This CallbackHandler is used for testing purposes only, to allow us to input the username/password in code.
     */
    public class TestHandler implements CallbackHandler {

        private String testPassword;
        private String testUsername;

        public void setTestPassword(String password) {
            testPassword = password;
        }

        public void setTestUsername(String username) {
            testUsername = username;
        }

        @Override
        public void handle(Callback[] callbacks) throws IOException, UnsupportedCallbackException {
            for (Callback callback : callbacks) {
                if (callback instanceof NameCallback) {
                    NameCallback nameCallback = (NameCallback) callback;
                    nameCallback.setName(testUsername);
                } else if (callback instanceof PasswordCallback) {
                    PasswordCallback passwordCallback = (PasswordCallback) callback;
                    passwordCallback.setPassword(testPassword.toCharArray());
                } else {
                    throw new UnsupportedCallbackException(callback);
                }
            }
        }
    }
}
