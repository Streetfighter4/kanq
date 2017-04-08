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
import {LoggedInGuard} from './guards/logged_in_guard';
import {FeedModule} from './feed/feed.module';
import {TopicIndexModule} from './topic/topic-index/topic-index.module';
import {HttpClient} from './http_client/http-client.service';
import {HttpModule} from '@angular/http';
import {TopicDetailModule} from './topic/topic-detail/topic-detail.module';

@NgModule({
  imports: [
    BrowserModule,
    TopicIndexModule,
    TopicDetailModule,
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
