// Code generated by protoc-gen-go. DO NOT EDIT.
// source: attendance_code.proto

package rpc

import (
	fmt "fmt"
	proto "github.com/golang/protobuf/proto"
	_ "github.com/golang/protobuf/ptypes/wrappers"
	math "math"
)

// Reference imports to suppress errors if they are not otherwise used.
var _ = proto.Marshal
var _ = fmt.Errorf
var _ = math.Inf

// This is a compile-time assertion to ensure that this generated file
// is compatible with the proto package it is being compiled against.
// A compilation error at this line likely means your copy of the
// proto package needs to be updated.
const _ = proto.ProtoPackageIsVersion3 // please upgrade the proto package

type AttendanceCodeCreate struct {
	MinutesToLive        int64    `protobuf:"varint,1,opt,name=minutesToLive,proto3" json:"minutesToLive,omitempty"`
	XXX_NoUnkeyedLiteral struct{} `json:"-"`
	XXX_unrecognized     []byte   `json:"-"`
	XXX_sizecache        int32    `json:"-"`
}

func (m *AttendanceCodeCreate) Reset()         { *m = AttendanceCodeCreate{} }
func (m *AttendanceCodeCreate) String() string { return proto.CompactTextString(m) }
func (*AttendanceCodeCreate) ProtoMessage()    {}
func (*AttendanceCodeCreate) Descriptor() ([]byte, []int) {
	return fileDescriptor_afd17f95304ceece, []int{0}
}

func (m *AttendanceCodeCreate) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_AttendanceCodeCreate.Unmarshal(m, b)
}
func (m *AttendanceCodeCreate) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_AttendanceCodeCreate.Marshal(b, m, deterministic)
}
func (m *AttendanceCodeCreate) XXX_Merge(src proto.Message) {
	xxx_messageInfo_AttendanceCodeCreate.Merge(m, src)
}
func (m *AttendanceCodeCreate) XXX_Size() int {
	return xxx_messageInfo_AttendanceCodeCreate.Size(m)
}
func (m *AttendanceCodeCreate) XXX_DiscardUnknown() {
	xxx_messageInfo_AttendanceCodeCreate.DiscardUnknown(m)
}

var xxx_messageInfo_AttendanceCodeCreate proto.InternalMessageInfo

func (m *AttendanceCodeCreate) GetMinutesToLive() int64 {
	if m != nil {
		return m.MinutesToLive
	}
	return 0
}

type AttendanceCode struct {
	Code                 int64    `protobuf:"varint,1,opt,name=code,proto3" json:"code,omitempty"`
	Unix                 int64    `protobuf:"varint,2,opt,name=unix,proto3" json:"unix,omitempty"`
	XXX_NoUnkeyedLiteral struct{} `json:"-"`
	XXX_unrecognized     []byte   `json:"-"`
	XXX_sizecache        int32    `json:"-"`
}

func (m *AttendanceCode) Reset()         { *m = AttendanceCode{} }
func (m *AttendanceCode) String() string { return proto.CompactTextString(m) }
func (*AttendanceCode) ProtoMessage()    {}
func (*AttendanceCode) Descriptor() ([]byte, []int) {
	return fileDescriptor_afd17f95304ceece, []int{1}
}

func (m *AttendanceCode) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_AttendanceCode.Unmarshal(m, b)
}
func (m *AttendanceCode) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_AttendanceCode.Marshal(b, m, deterministic)
}
func (m *AttendanceCode) XXX_Merge(src proto.Message) {
	xxx_messageInfo_AttendanceCode.Merge(m, src)
}
func (m *AttendanceCode) XXX_Size() int {
	return xxx_messageInfo_AttendanceCode.Size(m)
}
func (m *AttendanceCode) XXX_DiscardUnknown() {
	xxx_messageInfo_AttendanceCode.DiscardUnknown(m)
}

var xxx_messageInfo_AttendanceCode proto.InternalMessageInfo

func (m *AttendanceCode) GetCode() int64 {
	if m != nil {
		return m.Code
	}
	return 0
}

func (m *AttendanceCode) GetUnix() int64 {
	if m != nil {
		return m.Unix
	}
	return 0
}

func init() {
	proto.RegisterType((*AttendanceCodeCreate)(nil), "rpc.AttendanceCodeCreate")
	proto.RegisterType((*AttendanceCode)(nil), "rpc.AttendanceCode")
}

func init() {
	proto.RegisterFile("attendance_code.proto", fileDescriptor_afd17f95304ceece)
}

var fileDescriptor_afd17f95304ceece = []byte{
	// 227 bytes of a gzipped FileDescriptorProto
	0x1f, 0x8b, 0x08, 0x00, 0x00, 0x00, 0x00, 0x00, 0x02, 0xff, 0xe2, 0x12, 0x4d, 0x2c, 0x29, 0x49,
	0xcd, 0x4b, 0x49, 0xcc, 0x4b, 0x4e, 0x8d, 0x4f, 0xce, 0x4f, 0x49, 0xd5, 0x2b, 0x28, 0xca, 0x2f,
	0xc9, 0x17, 0x62, 0x2e, 0x2a, 0x48, 0x96, 0x92, 0x4b, 0xcf, 0xcf, 0x4f, 0xcf, 0x49, 0xd5, 0x07,
	0x0b, 0x25, 0x95, 0xa6, 0xe9, 0x97, 0x17, 0x25, 0x16, 0x14, 0xa4, 0x16, 0x15, 0x43, 0x14, 0x29,
	0xd9, 0x70, 0x89, 0x38, 0xc2, 0x75, 0x3b, 0xe7, 0xa7, 0xa4, 0x3a, 0x17, 0xa5, 0x26, 0x96, 0xa4,
	0x0a, 0xa9, 0x70, 0xf1, 0xe6, 0x66, 0xe6, 0x95, 0x96, 0xa4, 0x16, 0x87, 0xe4, 0xfb, 0x64, 0x96,
	0xa5, 0x4a, 0x30, 0x2a, 0x30, 0x6a, 0x30, 0x07, 0xa1, 0x0a, 0x2a, 0x59, 0x70, 0xf1, 0xa1, 0xea,
	0x16, 0x12, 0xe2, 0x62, 0x01, 0x39, 0x01, 0xaa, 0x1c, 0xcc, 0x06, 0x89, 0x95, 0xe6, 0x65, 0x56,
	0x48, 0x30, 0x41, 0xc4, 0x40, 0x6c, 0xa3, 0x15, 0x8c, 0x5c, 0xc2, 0xa8, 0x5a, 0x03, 0xc0, 0x8e,
	0xf6, 0xe4, 0x12, 0x75, 0x4f, 0x2d, 0x41, 0x95, 0x71, 0xaa, 0xf4, 0x4c, 0x11, 0x92, 0xd6, 0x83,
	0xf8, 0x44, 0x0f, 0xe6, 0x13, 0x3d, 0xcf, 0xbc, 0x12, 0x33, 0x93, 0xb0, 0xc4, 0x9c, 0xd2, 0x54,
	0x29, 0x61, 0xbd, 0xa2, 0x82, 0x64, 0x3d, 0x34, 0xa7, 0xb8, 0x71, 0x89, 0x40, 0x3c, 0x83, 0x26,
	0x2e, 0x89, 0x45, 0x31, 0x44, 0x21, 0x56, 0x73, 0x9c, 0x38, 0x57, 0x31, 0xb1, 0x81, 0x1d, 0x57,
	0x9c, 0xc4, 0x06, 0xb6, 0xdc, 0x18, 0x10, 0x00, 0x00, 0xff, 0xff, 0xd4, 0x1d, 0xd9, 0x11, 0x72,
	0x01, 0x00, 0x00,
}
