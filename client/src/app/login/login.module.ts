import {NgModule} from '@angular/core';
import {LoginComponent} from './login.component';
import {FormsModule} from '@angular/forms';
import {AlertModule} from 'ng2-bootstrap';
import {BrowserModule} from '@angular/platform-browser';
import {RouterModule} from '@angular/router';

@NgModule({
  imports: [
    AlertModule,
    FormsModule,
    BrowserModule,
    RouterModule
  ],
  declarations: [
    LoginComponent
  ]
})
export class LoginModule {}
