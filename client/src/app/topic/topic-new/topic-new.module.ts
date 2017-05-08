import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import {TopicNewComponent} from './topic-new.component';
import {InfiniteScrollModule} from 'ngx-infinite-scroll';
import {RouterModule} from '@angular/router';

@NgModule({
  imports: [
    CommonModule,
    InfiniteScrollModule,
    RouterModule
  ],
  declarations: [
    TopicNewComponent
  ],
  exports: [
    TopicNewComponent
  ]
})
export class TopicNewModule { }
