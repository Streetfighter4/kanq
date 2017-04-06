import {Injectable} from '@angular/core';
import {CanActivate, Router} from '@angular/router';
import {UserService} from '../user/user.service';

@Injectable()
export class LoggedInGuard implements CanActivate {
  constructor(private userService: UserService,
              private router: Router) {}

  canActivate() {
    let loggedIn = this.userService.isLoggedIn();

    if(!loggedIn) {
      this.router.navigate(['/']);
    }

    return loggedIn;
  }
}
