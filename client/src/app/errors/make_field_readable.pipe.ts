import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'make_field_readable'
})
export class MakeFieldReadablePipe implements PipeTransform {
  transform(value: any, args?: any): any {
    if(value === null) {
      return 'Not assigned';
    }

    let name = value.charAt(0).toUpperCase() + value.slice(1);
    name = name.replace('_', ' ');

    return name;
  }
}
