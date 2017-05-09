import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import {TopicNewComponent} from './topic-new.component';
import {InfiniteScrollModule} from 'ngx-infinite-scroll';
import {RouterModule} from '@angular/router';
import {TopicNavModule} from '../topic-nav/topic-nav.module';
import {PostGlanceModule} from '../../post/post-glance/post-glance.module';
import {PostCreateModule} from '../../post/post-create/post-create.module';

@NgModule({
  imports: [
    CommonModule,
    InfiniteScrollModule,
    RouterModule,
    TopicNavModule,
    PostGlanceModule,
    PostCreateModule
  ],
  declarations: [
    TopicNewComponent
  ],
  exports: [
    TopicNewComponent
  ]
})
export class TopicNewModule { }
