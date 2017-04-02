import { NgModule }      from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent }  from './app.component';
import {RouterModule} from '@angular/router';
import {FacebookModule} from './oauth/facebook/facebook.module';
import {NavbarModule} from './navbar/navbar.module';
import {LoginModule} from './login/login.module';
import {AlertModule} from 'ng2-bootstrap';
import {HomeModule} from './home/home.module';
import {ROUTES} from './routes';

@NgModule({
  imports: [
    BrowserModule,
    RouterModule.forRoot(ROUTES),
    FacebookModule,
    NavbarModule,
    LoginModule,
    HomeModule,
    AlertModule.forRoot(),
  ],
  declarations: [
    AppComponent,
  ],
  bootstrap: [ AppComponent ]
})
export class AppModule { }
