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
import {SignupModule} from './signup/signup.module';
import {LoggedInGuard} from './common/logged_in_guard';
import {FeedModule} from './feed/feed.module';
import {TopicIndexModule} from './topic/topic-index/topic-index.module';
import {HttpClient} from './common/http-client.service';
import {HttpModule} from '@angular/http';
import {PostDetailModule} from './post/post-detail/post-detail.module';
import {NotFoundModule} from './common/not-found/not-found.module';
import {TopicNewModule} from './topic/topic-new/topic-new.module';
import {TopicTrendingModule} from './topic/topic-trending/topic-trending.module';
import {TopicTopModule} from './topic/topic-top/topic-top.module';
import {TopicDetailModule} from './topic/topic-detail/topic-detail.module';

@NgModule({
  imports: [
    BrowserModule,
    TopicIndexModule,
    TopicNewModule,
    TopicTrendingModule,
    TopicTopModule,
    TopicDetailModule,
    PostDetailModule,
    NotFoundModule,
    RouterModule.forRoot(ROUTES),
    FacebookModule,
    NavbarModule,
    LoginModule,
    SignupModule,
    HomeModule,
    FeedModule,
    AlertModule.forRoot(),
    HttpModule
  ],
  declarations: [
    AppComponent,
  ],
  bootstrap: [ AppComponent ],
  providers: [
    LoggedInGuard,
    HttpClient,
  ]
})
export class AppModule { }
