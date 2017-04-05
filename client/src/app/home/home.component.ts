import {Component, OnInit} from '@angular/core';
import {UserService} from '../user/user.service';
import {Router} from '@angular/router';

@Component({
  moduleId: module.id,
  templateUrl: 'home.component.html'
})
export class HomeComponent implements OnInit {
  constructor(private userService: UserService,
              private router: Router) {}

  ngOnInit() {
    if(this.userService.isLoggedIn()) {
      this.router.navigate(['/feed']);
    }
  }
}
