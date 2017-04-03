import {Route} from '@angular/router';
import {HomeComponent} from './home/home.component';
import {LoginComponent} from './login/login.component';
import {FacebookAuthorizerComponent} from './oauth/facebook/facebook_authorizer.component';
import {FacebookTokenHandlerComponent} from './oauth/facebook/facebook_token_handler.component';
import {SignupComponent} from './signup/signup.component';

export const ROUTES: Route[] = [
  {
    path: '',
    component: HomeComponent
  },
  {
    path: 'login',
    component: LoginComponent
  },
  {
    path: 'signup',
    component: SignupComponent
  },
  {
    path: 'oauth/facebook',
    children: [
      {
        path: 'authorize',
        component: FacebookAuthorizerComponent
      },
      {
        path: 'token',
        component: FacebookTokenHandlerComponent
      }
    ]
  }
];
