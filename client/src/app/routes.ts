import {Route} from '@angular/router';
import {HomeComponent} from './home/home.component';
import {LoginComponent} from './login/login.component';
import {FacebookAuthorizerComponent} from './oauth/facebook/facebook_authorizer.component';
import {FacebookTokenHandlerComponent} from './oauth/facebook/facebook_token_handler.component';
import {LoggedInGuard} from './guards/logged_in_guard';
import {FeedComponent} from './feed/feed.component';

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
    path: 'feed',
    component: FeedComponent,
    canActivate: [LoggedInGuard]
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
