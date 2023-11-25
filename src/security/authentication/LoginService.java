package security.authentication;
import javax.security.auth.Subject;
import javax.security.auth.login.LoginContext;
import javax.security.auth.login.LoginException;

import security.authentication.ConsoleCallbackHandler;

public class LoginService {

    public Subject login() throws LoginException {
        LoginContext loginContext = new LoginContext("jaasApplication", new ConsoleCallbackHandler());
        loginContext.login();
        return loginContext.getSubject();
    }
}