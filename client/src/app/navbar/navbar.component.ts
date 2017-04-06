import {Component} from '@angular/core';
import {UserService} from '../user/user.service';
import {Router} from '@angular/router';

@Component({
  moduleId: module.id,
  selector: 'navbar',
  templateUrl: 'navbar.component.html',
})
export class NavbarComponent {
  constructor(private userService: UserService,
              private router: Router) {}

  signout() {
    this.userService.signout();
    this.router.navigate(['/']);
  }
}
