import { NgModule }      from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent }  from './app.component';
import {FacebookAuthorizerComponent} from './oauth/facebook/facebook_authorizer.component';
import {AppRoutingModule} from './app-routing.module';
import {HttpModule} from '@angular/http';
import {FacebookTokenHandlerComponent} from './oauth/facebook/facebook_token_handler.component';
import {DeviantArtAuthorizerComponent} from './oauth/deviant_art/deviant_art_authorizer.component';
import {DeviantArtTokenHandlerComponent} from './oauth/deviant_art/deviant_art_token_handler.component';

@NgModule({
  imports:      [
    BrowserModule,
    AppRoutingModule,
    HttpModule
  ],
  declarations: [
    AppComponent,
    FacebookAuthorizerComponent,
    FacebookTokenHandlerComponent,
    DeviantArtAuthorizerComponent,
    DeviantArtTokenHandlerComponent
  ],
  bootstrap:    [ AppComponent ]
})
export class AppModule { }
