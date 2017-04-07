import {NgModule} from '@angular/core';
import {FacebookAuthorizerComponent} from './facebook_authorizer.component';
import {FacebookTokenHandlerComponent} from './facebook_token_handler.component';
import {FacebookService} from './facebook.service';
import {UserService} from '../../user/user.service';

@NgModule({
  declarations: [
    FacebookAuthorizerComponent,
    FacebookTokenHandlerComponent
  ],
  providers: [
    FacebookService,
    UserService
  ]
})
export class FacebookModule {}
