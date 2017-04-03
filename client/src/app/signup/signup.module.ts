import {NgModule} from '@angular/core';
import {FormsModule} from '@angular/forms';
import {AlertModule} from 'ng2-bootstrap';
import {BrowserModule} from '@angular/platform-browser';
import {RouterModule} from '@angular/router';
import {SignupComponent} from './signup.component';

@NgModule({
  imports: [
    AlertModule,
    FormsModule,
    BrowserModule,
    RouterModule
  ],
  declarations: [
    SignupComponent
  ]
})
export class SignupModule {}
