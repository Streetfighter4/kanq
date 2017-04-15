import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import {TopicIndexComponent} from './topic-index.component';
import {TopicService} from '../topic/topic.service';
import {RouterModule} from '@angular/router';

@NgModule({
  imports: [
    CommonModule,
    RouterModule
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
