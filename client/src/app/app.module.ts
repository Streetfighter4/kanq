import { NgModule }      from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent }  from './app.component';
import {RouterModule} from '@angular/router';
import {FacebookModule} from './oauth/facebook/facebook.module';
import {NavbarModule} from './navbar/navbar.module';
import {Ng2BootstrapModule} from 'ng2-bootstrap';

@NgModule({
  imports:      [
    BrowserModule,
    RouterModule.forRoot([]),
    FacebookModule,
    NavbarModule,
    Ng2BootstrapModule.forRoot()
  ],
  declarations: [
    AppComponent,
  ],
  bootstrap:    [ AppComponent ]
})
export class AppModule { }
