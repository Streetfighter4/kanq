import {NgModule} from '@angular/core';
import {FacebookAuthorizerComponent} from './facebook_authorizer.component';
import {FacebookTokenHandlerComponent} from './facebook_token_handler.component';
import {RouterModule} from '@angular/router';
import {ROUTES} from './facebook-routes.config';
import {HttpModule} from '@angular/http';

@NgModule({
  imports: [
    RouterModule.forChild(ROUTES),
    HttpModule
  ],
  declarations: [
    FacebookAuthorizerComponent,
    FacebookTokenHandlerComponent
  ]
})
export class FacebookModule {}
