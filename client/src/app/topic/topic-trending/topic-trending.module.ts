import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import {InfiniteScrollModule} from 'ngx-infinite-scroll';
import {RouterModule} from '@angular/router';
import {TopicTrendingComponent} from './topic-trending.component';
import {TopicNavModule} from '../topic-nav/topic-nav.module';
import {PostGlanceModule} from '../../post/post-glance/post-glance.module';

@NgModule({
  imports: [
    CommonModule,
    InfiniteScrollModule,
    RouterModule,
    TopicNavModule,
    PostGlanceModule
  ],
  declarations: [
    TopicTrendingComponent
  ],
  exports: [
    TopicTrendingComponent
  ]
})
export class TopicTrendingModule { }
