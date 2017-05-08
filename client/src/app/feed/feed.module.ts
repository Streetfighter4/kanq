import {NgModule} from '@angular/core';
import {FeedComponent} from './feed.component';
import {PaginatedListModule} from '../paginated-list/paginated-list.module';
import {PostService} from '../post/post.service';
import {FormsModule} from '@angular/forms';
import {CommonModule} from '@angular/common';
import {BrowserModule} from '@angular/platform-browser';
import {InfiniteScrollModule} from 'ngx-infinite-scroll';
import {RouterModule} from '@angular/router';
import {PostGlanceModule} from '../post/post-glance/post-glance.module';

@NgModule({
  imports: [
    PaginatedListModule,
    CommonModule,
    BrowserModule,
    FormsModule,
    InfiniteScrollModule,
    RouterModule,
    PostGlanceModule
  ],
  declarations: [
    FeedComponent
  ],
  exports: [
    FeedComponent
  ],
  providers: [
    PostService
  ]
})
export class FeedModule { }
