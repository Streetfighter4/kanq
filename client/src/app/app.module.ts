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
import {LoggedInGuard} from './guards/logged_in_guard';
import {FeedModule} from './feed/feed.module';
import {TopicIndexModule} from './topic/topic-index/topic-index.module';

@NgModule({
  imports: [
    BrowserModule,
    TopicIndexModule,
    RouterModule.forRoot(ROUTES),
    FacebookModule,
    NavbarModule,
    LoginModule,
    HomeModule,
    FeedModule,
    AlertModule.forRoot(),
  ],
  declarations: [
    AppComponent,
  ],
  bootstrap: [ AppComponent ],
  providers: [
    LoggedInGuard
  ]
})
export class AppModule { }
