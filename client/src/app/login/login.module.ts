import {NgModule} from '@angular/core';
import {RouterModule} from '@angular/router';
import {ROUTES} from './login-routes.config';
import {LoginComponent} from './login.component';
import {FormsModule} from '@angular/forms';

@NgModule({
  imports: [
    RouterModule.forRoot(ROUTES),
    FormsModule
  ],
  declarations: [
    LoginComponent
  ]
})
export class LoginModule {}
