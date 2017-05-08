import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import {TopicIndexComponent} from './topic-index.component';
import {TopicService} from '../topic.service';
import {RouterModule} from '@angular/router';
import {InfiniteScrollModule} from 'ngx-infinite-scroll';

@NgModule({
  imports: [
    CommonModule,
    RouterModule,
    InfiniteScrollModule
  ],
  declarations: [
    TopicIndexComponent
  ],
  exports: [
    TopicIndexComponent
  ],
  providers: [
    TopicService
  ],
})
export class TopicIndexModule { }
