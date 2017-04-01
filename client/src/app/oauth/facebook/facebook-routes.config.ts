import {Route} from '@angular/router';
import {FacebookTokenHandlerComponent} from './facebook_token_handler.component';
import {FacebookAuthorizerComponent} from './facebook_authorizer.component';

export const ROUTES: Route[] = [
  {path: 'oauth/facebook/authorize', component: FacebookAuthorizerComponent},
  {path: 'oauth/facebook/token', component: FacebookTokenHandlerComponent}
];
