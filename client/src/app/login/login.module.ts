import {NgModule} from '@angular/core';
import {RouterModule} from '@angular/router';
import {ROUTES} from './login-routes.config';
import {LoginComponent} from './login.component';
import {FormsModule} from '@angular/forms';
import {AlertModule} from 'ng2-bootstrap';

@NgModule({
  imports: [
    RouterModule.forRoot(ROUTES),
    FormsModule,
    AlertModule
  ],
  declarations: [
    LoginComponent
  ]
})
export class LoginModule {}
