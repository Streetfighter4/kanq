import {Component, OnInit} from '@angular/core';
import {User} from '../user/user';

@Component({
  moduleId: module.id,
  templateUrl: 'login.component.html'
})
export class LoginComponent implements OnInit {
  user: User;

  login() {
    console.log(this.user);
  }

  ngOnInit() {
    this.user = new User();
  }
}
