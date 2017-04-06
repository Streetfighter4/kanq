import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import {ErrorFieldsPipe} from './error-fields.pipe';
import {ErrorsComponent} from './errors.component';
import {AlertModule} from 'ng2-bootstrap';
import {MakeFieldReadablePipe} from './make_field_readable.pipe';

@NgModule({
  imports: [
    CommonModule,
    AlertModule
  ],
  declarations: [
    ErrorFieldsPipe,
    ErrorsComponent,
    MakeFieldReadablePipe
  ],
  exports: [
    ErrorsComponent
  ]
})
export class ErrorsModule { }
