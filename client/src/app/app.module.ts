import { NgModule }      from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent }  from './app.component';
import {FacebookAuthorizerComponent} from './oauth/facebook/facebook_authorizer.component';
import {AppRoutingModule} from './app-routing.module';
import {HttpModule} from '@angular/http';
import {FacebookTokenComponent} from './oauth/facebook/facebook_token.component';

@NgModule({
  imports:      [
    BrowserModule,
    AppRoutingModule,
    HttpModule
  ],
  declarations: [
    AppComponent,
    FacebookAuthorizerComponent,
    FacebookTokenComponent
  ],
  bootstrap:    [ AppComponent ]
})
export class AppModule { }
