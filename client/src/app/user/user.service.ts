import {Injectable} from '@angular/core';
import {Settings} from '../settings';
import {User} from './user';
import {Router} from '@angular/router';
import {HttpClient} from '../http_client/http-client.service';

@Injectable()
export class UserService {
  constructor(private http: HttpClient,
              private router: Router) {}

  loginThroughToken(token: string, backend: string): Promise<string> {
    let body = {
      client_id: Settings.API_CLIENT_ID,
      client_secret: Settings.API_SECRET,
      grant_type: Settings.API_CONVERT_TOKEN_GRANT,
      backend: backend,
      token: token
    };

    return this.http.post(Settings.API_CONVERT_TOKEN_URL, body)
      .toPromise()
      .then(res => res.json().access_token)
      .catch(err => console.log('Login through token error', err));
  }

  loginThroughPassword(user: User): Promise<any> {
    let body = {
      username: user.username,
      password: user.password
    };

    return this.http.post(Settings.API_PASSWORD_LOGIN_URL, body)
      .toPromise()
      .then(res => res.json().token);
  }

  isLoggedIn(): boolean {
    let token = localStorage.getItem(Settings.LOCAL_STORAGE_TOKEN_KEY);
    return token != undefined;
  }

  signout() {
    localStorage.removeItem(Settings.LOCAL_STORAGE_TOKEN_KEY)
  }
}
