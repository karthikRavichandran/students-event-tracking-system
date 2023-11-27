package security.authentication;
import javax.security.auth.Subject;
import javax.security.auth.login.LoginContext;
import javax.security.auth.login.LoginException;
import javax.security.auth.callback.CallbackHandler;

import security.authentication.ConsoleCallbackHandler;

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
}