import {Component} from '@angular/core';
import {UserService} from '../user/user.service';

@Component({
  moduleId: module.id,
  selector: 'navbar',
  templateUrl: 'navbar.component.html',
})
export class NavbarComponent {
  constructor(private userService: UserService) {}
}
