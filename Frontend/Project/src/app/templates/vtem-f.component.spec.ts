import { ComponentFixture, TestBed } from '@angular/core/testing';

import { VTemFComponent } from './vtem-f.component';

describe('VTemFComponent', () => {
  let component: VTemFComponent;
  let fixture: ComponentFixture<VTemFComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ VTemFComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(VTemFComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
