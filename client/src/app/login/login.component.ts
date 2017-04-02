import {Component, OnInit} from '@angular/core';
import {User} from '../user/user';
import {UserService} from '../user/user.service';
import {Settings} from '../settings';
import {Router} from '@angular/router';

@Component({
  moduleId: module.id,
  templateUrl: 'login.component.html'
})
export class LoginComponent {
  user: User = new User();
  errors: any;

  constructor(private userService: UserService,
              private router: Router) {}

  login() {
    this.userService.loginThroughPassword(this.user)
      .then(this.handleLoginSuccess.bind(this))
      .catch(this.handleLoginError);
  }

  handleLoginSuccess(token) {
    console.log('Successful login', token);
    localStorage.setItem(Settings.LOCAL_STORAGE_TOKEN_KEY, token);
    this.router.navigate(['/'])
  }

  handleLoginError(res) {
    console.log(res);
    this.errors = res;
  }
}
