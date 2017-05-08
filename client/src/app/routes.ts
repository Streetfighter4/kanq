import {Route} from '@angular/router';
import {HomeComponent} from './home/home.component';
import {LoginComponent} from './login/login.component';
import {FacebookAuthorizerComponent} from './oauth/facebook/facebook_authorizer.component';
import {FacebookTokenHandlerComponent} from './oauth/facebook/facebook_token_handler.component';
import {SignupComponent} from './signup/signup.component';
import {LoggedInGuard} from './common/logged_in_guard';
import {FeedComponent} from './feed/feed.component';
import {TopicIndexComponent} from './topic/topic-index/topic-index.component';
import {PostDetailComponent} from './post/post-detail/post-detail.component';
import {NotFoundComponent} from './common/not-found/not-found.component';
import {TopicNewComponent} from './topic/topic-new/topic-new.component';
import {TopicTrendingComponent} from './topic/topic-trending/topic-trending.component';
import {TopicTopComponent} from './topic/topic-top/topic-top.component';

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
    path: 'feed',
    component: FeedComponent,
    canActivate: [LoggedInGuard]
  },
  {
    path: 'topics',
    component: TopicIndexComponent,
    canActivate: [LoggedInGuard],
  },
  {
    path: 'topics/:id',
    canActivate: [LoggedInGuard],
    children: [
      {
        path: 'new',
        component: TopicNewComponent,
      },
      {
        path: 'trending',
        component: TopicTrendingComponent
      },
      {
        path: 'top',
        component: TopicTopComponent
      }
    ]
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
  },
  {
    path: 'posts/:id',
    component: PostDetailComponent,
    canActivate: [LoggedInGuard]
  },
  {
    path: '404',
    component: NotFoundComponent
  },
  {
    path: '**',
    redirectTo: '404'
  }
];
