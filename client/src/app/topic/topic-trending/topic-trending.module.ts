import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import {InfiniteScrollModule} from 'ngx-infinite-scroll';
import {RouterModule} from '@angular/router';
import {TopicTrendingComponent} from './topic-trending.component';

@NgModule({
  imports: [
    CommonModule,
    InfiniteScrollModule,
    RouterModule
  ],
  declarations: [
    TopicTrendingComponent
  ],
  exports: [
    TopicTrendingComponent
  ]
})
export class TopicTrendingModule { }
